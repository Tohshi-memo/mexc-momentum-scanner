# Decision Report

- generated_at: 2026-05-30T04:25:32.580962+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5103**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5103, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-2.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.32% | **-2.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 6/20 | 30.0% | +7.43% | **+2.23%** |
| LIMIT_10PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.73% | **+0.96%** |
| LIMIT_7PCT | 7/20 | 35.0% | +0.63% | **+0.22%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.32% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.96% | **+2.96%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.20% | **+2.56%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.98% | **+1.94%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +4.15% | **+1.87%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.00% | **+1.65%** |

## 2. $100 Live Portfolio

- 残高: **$98.10** / 初期 $100.00 (-1.90%)
- 確定トレード: 75件 (TP 22 / SL 50 / EXP 3)
- 最新: ESPORTS/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.10
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.64** / 初期 $100.00 (+26.64%)
- 確定: 761件 (Win 177 / Loss 227 / Flat 357) / skip 903件
- 成長率目線: 平均log +0.000310 / 幾何平均 +0.031% per trade / maxDD +4.72%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $126.64

## 4. Latest Market Context

- 更新: 2026-05-30T04:25:27.062171+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=73381.4
- Funnel: target 773 → liquid 147 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +57.36% | $11,807,806.17 |
| XLM/USDT:USDT | +30.15% | $462,523,197.87 |
| ID/USDT:USDT | +26.35% | $6,019,772.21 |
| OL/USDT:USDT | +18.50% | $1,520,586.64 |
| LAB/USDT:USDT | +17.89% | $137,765,669.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HEI/USDT:USDT | below_1h_threshold | +1.61% | +1.77% |
| BEAT/USDT:USDT | below_1h_threshold | +1.25% | +1.40% |
| XMR/USDT:USDT | below_1h_threshold | +0.90% | +1.05% |
| CTR/USDT:USDT | below_1h_threshold | +0.76% | +0.91% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
