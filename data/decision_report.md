# Decision Report

- generated_at: 2026-05-13T08:58:14.763165+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4204**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4204, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |
| ASK | 20/20 | 100.0% | +0.34% | **+0.34%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.43% | **+0.32%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.22% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.36% | **+1.22%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.24% | **+0.62%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.63% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$97.71** / 初期 $100.00 (-2.29%)
- 確定トレード: 37件 (TP 9 / SL 25 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.80** / 初期 $100.00 (+19.80%)
- 確定: 340件 (Win 94 / Loss 123 / Flat 123) / skip 425件
- 成長率目線: 平均log +0.000531 / 幾何平均 +0.053% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.20% 残高後 $119.80

## 4. Latest Market Context

- 更新: 2026-05-13T08:58:05.852331+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=81134.1
- Funnel: target 764 → liquid 190 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.6 >= 65=1, 4h RSI 70.7 >= 65=1, 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COS/USDT:USDT | +42.75% | $1,524,988.62 |
| IRYS/USDT:USDT | +28.77% | $6,745,178.97 |
| LAB/USDT:USDT | +26.70% | $109,476,559.13 |
| UB/USDT:USDT | +23.73% | $5,049,826.17 |
| SATO/USDT:USDT | +21.01% | $1,310,501.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +2.98% | +2.79% |
| KITE/USDT:USDT | below_1h_threshold | +2.88% | +2.69% |
| TURBO/USDT:USDT | below_1h_threshold | +2.21% | +2.02% |
| JTO/USDT:USDT | below_1h_threshold | +1.82% | +1.63% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.62% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
