# Decision Report

- generated_at: 2026-05-12T14:43:11.412595+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4130**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4130, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.37% | **-0.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.12%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | -0.30% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.57% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.55% | **+0.55%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.76% | **+0.38%** |
| ASK_LONG | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.41% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$118.26** / 初期 $100.00 (+18.26%)
- 確定: 266件 (Win 74 / Loss 90 / Flat 102) / skip 425件
- 成長率目線: 平均log +0.000631 / 幾何平均 +0.063% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GIGA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $118.26

## 4. Latest Market Context

- 更新: 2026-05-12T14:43:07.514682+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.48% price=80815.7
- Funnel: target 763 → liquid 196 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1, 4h RSI 82.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +82.41% | $28,172,246.17 |
| GIGA/USDT:USDT | +68.48% | $7,507,928.94 |
| SKYAI/USDT:USDT | +41.45% | $40,261,693.64 |
| GUA/USDT:USDT | +34.74% | $3,743,412.69 |
| USELESS/USDT:USDT | +34.52% | $11,033,220.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.47% | +3.99% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.77% | +3.29% |
| CYS/USDT:USDT | below_1h_threshold | +2.59% | +2.11% |
| FF/USDT:USDT | below_1h_threshold | +2.51% | +2.03% |
| SAHARA/USDT:USDT | below_1h_threshold | +1.88% | +1.41% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
