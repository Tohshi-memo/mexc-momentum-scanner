# Decision Report

- generated_at: 2026-05-17T12:28:28.324490+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4399**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4399, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.35% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.42% | **+0.34%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.22% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.62% | **+1.13%** |
| ASK_LONG | 20/20 | 100.0% | +0.90% | **+0.90%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.12% | **+0.73%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.76% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.24** / 初期 $100.00 (+18.24%)
- 確定: 397件 (Win 101 / Loss 137 / Flat 159) / skip 563件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIA/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $118.24

## 4. Latest Market Context

- 更新: 2026-05-17T12:28:25.844623+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78383.1
- Funnel: target 760 → liquid 116 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +43.73% | $10,911,768.53 |
| AIA/USDT:USDT | +29.82% | $14,243,294.47 |
| CGPT/USDT:USDT | +19.70% | $2,408,381.50 |
| KAIA/USDT:USDT | +14.39% | $1,886,505.64 |
| ASTEROID/USDT:USDT | +13.48% | $4,507,061.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.37% | +2.36% |
| LAB/USDT:USDT | below_1h_threshold | +1.71% | +1.70% |
| CGPT/USDT:USDT | below_1h_threshold | +1.67% | +1.66% |
| BEAT/USDT:USDT | below_1h_threshold | +1.31% | +1.29% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.27% | +1.26% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
