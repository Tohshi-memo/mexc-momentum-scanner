# Decision Report

- generated_at: 2026-11-06T03:41:37.446280+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18236**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18236, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +5.41% | **+1.89%** |
| LIMIT_7PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_BB3S | 2/17 | 11.8% | +8.00% | **+0.94%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.29% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +5.11% | **+2.04%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +4.00% | **+1.40%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.70% | **+0.56%** |
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7762件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.94** / 初期 $100.00 (+273.94%)
- 確定: 4612件 (Win 1235 / Loss 1031 / Flat 2346) / skip 7035件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0191 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $373.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6397件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000272 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T03:41:18.441864+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.38% price=75875.1
- Funnel: target 1084 → liquid 187 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +53.97% | $8,544,277.09 |
| CYBER/USDT:USDT | +50.72% | $2,331,385.41 |
| AKE/USDT:USDT | +19.18% | $19,998,688.20 |
| IRENSTOCK/USDT:USDT | +17.22% | $3,136,107.93 |
| BLESS/USDT:USDT | +13.85% | $5,427,116.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.40% | +4.78% |
| KIOXIASTOCK/USDT:USDT | below_1h_threshold | +3.12% | +3.50% |
| BTW/USDT:USDT | below_1h_threshold | +3.03% | +3.40% |
| MUU/USDT:USDT | below_1h_threshold | +2.48% | +2.85% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.05% | +2.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
