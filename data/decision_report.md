# Decision Report

- generated_at: 2026-11-06T03:51:25.888480+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18238**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18238, expectancy=+0.03%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +4.63% | **+2.08%** |
| LIMIT_7PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_BB3S | 2/17 | 11.8% | +8.00% | **+0.94%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +6.49% | **+1.95%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.67% | **+1.40%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.28% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 263件 (TP 96 / SL 159 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,477.20** / 初期 $100.00 (+1377.20%)
- 確定: 7035件 (Win 2022 / Loss 2247 / Flat 2766) / skip 7764件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,477.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$373.94** / 初期 $100.00 (+273.94%)
- 確定: 4612件 (Win 1235 / Loss 1031 / Flat 2346) / skip 7037件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.25%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0155 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $373.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6399件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000111 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-06T03:51:12.384408+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=75905.6
- Funnel: target 1084 → liquid 188 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CYBER/USDT:USDT | +54.70% | $2,372,847.06 |
| UAI/USDT:USDT | +53.97% | $8,754,650.84 |
| AKE/USDT:USDT | +26.82% | $20,223,987.69 |
| IRENSTOCK/USDT:USDT | +17.62% | $3,138,355.33 |
| BLESS/USDT:USDT | +13.47% | $5,441,114.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +4.40% | +4.74% |
| MUU/USDT:USDT | below_1h_threshold | +2.48% | +2.81% |
| BTW/USDT:USDT | below_1h_threshold | +2.20% | +2.54% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.05% | +2.38% |
| TSMSTOCK/USDT:USDT | below_1h_threshold | +1.96% | +2.29% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
