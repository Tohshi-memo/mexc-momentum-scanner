# Decision Report

- generated_at: 2026-10-01T16:46:35.911545+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15923**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15923, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +5.92% | **+1.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.24% | **+0.56%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +4.58% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.02% | **+1.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.48% | **+1.61%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.48% | **+1.33%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.39% | **+0.97%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.74% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$120.63** / 初期 $100.00 (+20.63%)
- 確定トレード: 226件 (TP 82 / SL 137 / EXP 7)
- 最新: LONGXIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.63
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,299.33** / 初期 $100.00 (+1199.33%)
- 確定: 6032件 (Win 1787 / Loss 1942 / Flat 2303) / skip 6452件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,299.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.42** / 初期 $100.00 (+178.42%)
- 確定: 3576件 (Win 996 / Loss 826 / Flat 1754) / skip 5758件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1570 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $278.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4089件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000348 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T16:46:24.472374+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=84374.9
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +11.12% | $24,289,575.35 |
| NOM/USDT:USDT | +3.71% | $3,068,832.63 |
| US/USDT:USDT | +3.61% | $1,465,965.68 |
| ZRO/USDT:USDT | +3.00% | $4,557,179.72 |
| SI/USDT:USDT | +2.72% | $6,739,203.12 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NOM/USDT:USDT | below_1h_threshold | +3.71% | +3.42% |
| US/USDT:USDT | below_1h_threshold | +3.59% | +3.29% |
| ZRO/USDT:USDT | below_1h_threshold | +3.01% | +2.71% |
| SI/USDT:USDT | below_1h_threshold | +2.73% | +2.43% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.45% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
