# Decision Report

- generated_at: 2026-08-05T07:21:28.831910+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10376**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10376, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.42% | **+0.40%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +2.28% | **+2.00%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.99% | **+0.90%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.89% | **+0.80%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.87% | **+0.75%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$614.48** / 初期 $100.00 (+514.48%)
- 確定: 3766件 (Win 1195 / Loss 1233 / Flat 1338) / skip 3171件
- 成長率目線: 平均log +0.000482 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HFT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $614.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$144.03** / 初期 $100.00 (+44.03%)
- 確定: 1309件 (Win 369 / Loss 306 / Flat 634) / skip 2478件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1088 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $144.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.79** / 初期 $100.00 (+18.79%)
- 確定: 1124件 (Win 361 / Loss 433 / Flat 330) / pending 5件 / skip 721件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HFT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.79

## 6. Latest Market Context

- 更新: 2026-08-05T07:21:19.538534+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=64065.8
- Funnel: target 939 → liquid 182 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HFT/USDT:USDT | +65.63% | $1,849,695.35 |
| BLESS/USDT:USDT | +60.64% | $27,027,164.53 |
| HEI/USDT:USDT | +50.00% | $15,864,499.95 |
| BICO/USDT:USDT | +36.04% | $17,087,337.31 |
| MARSCOIN/USDT:USDT | +33.51% | $1,194,640.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +3.39% | +3.64% |
| TAKE/USDT:USDT | below_1h_threshold | +2.17% | +2.42% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.87% | +2.12% |
| UNITREE/USDT:USDT | below_1h_threshold | +1.49% | +1.74% |
| BLESS/USDT:USDT | below_1h_threshold | +1.38% | +1.63% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
