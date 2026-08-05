# Decision Report

- generated_at: 2026-08-05T04:56:34.739357+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10362**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10362, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +4.24% | **+4.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.03% | **+1.93%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.93% | **+1.54%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.80% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$607.71** / 初期 $100.00 (+507.71%)
- 確定: 3759件 (Win 1192 / Loss 1230 / Flat 1337) / skip 3164件
- 成長率目線: 平均log +0.000480 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $607.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.22** / 初期 $100.00 (+42.22%)
- 確定: 1298件 (Win 365 / Loss 303 / Flat 630) / skip 2475件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1053 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $142.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.60** / 初期 $100.00 (+18.60%)
- 確定: 1114件 (Win 359 / Loss 430 / Flat 325) / pending 5件 / skip 719件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000394 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: GRVT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $118.60

## 6. Latest Market Context

- 更新: 2026-08-05T04:56:21.712301+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64129.6
- Funnel: target 939 → liquid 186 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI 68.4 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +88.86% | $10,123,072.36 |
| HFT/USDT:USDT | +45.95% | $1,236,522.12 |
| TAKE/USDT:USDT | +36.09% | $1,586,699.38 |
| CASHCAT/USDT:USDT | +35.35% | $1,208,246.16 |
| BLESS/USDT:USDT | +32.40% | $24,057,923.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +3.49% | +3.51% |
| BLESS/USDT:USDT | below_1h_threshold | +3.45% | +3.48% |
| HEI/USDT:USDT | below_1h_threshold | +2.97% | +3.00% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +2.89% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +2.85% | +2.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
