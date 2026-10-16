# Decision Report

- generated_at: 2026-10-16T09:26:35.217504+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16789**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16789, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.39% | **+1.08%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.13% | **+1.07%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.71% | **+0.86%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.12% | **+0.77%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.63% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.40% | **+0.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.39% | **+0.70%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.89% | **+0.62%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.32% | **+0.50%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,254.65** / 初期 $100.00 (+1154.65%)
- 確定: 6315件 (Win 1849 / Loss 2027 / Flat 2439) / skip 7035件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,254.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$278.90** / 初期 $100.00 (+178.90%)
- 確定: 3681件 (Win 1027 / Loss 873 / Flat 1781) / skip 6519件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $278.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4951件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000266 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T09:26:18.733687+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=82100.9
- Funnel: target 1078 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +80.68% | $9,183,953.77 |
| CLAUDIA/USDT:USDT | +36.57% | $1,042,873.28 |
| ICNT/USDT:USDT | +19.68% | $1,366,509.03 |
| INJ/USDT:USDT | +14.12% | $79,420,317.87 |
| TIA/USDT:USDT | +13.89% | $43,450,206.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.72% | +4.85% |
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.99% | +3.12% |
| ARB/USDT:USDT | below_1h_threshold | +1.50% | +1.63% |
| RIVER/USDT:USDT | below_1h_threshold | +0.73% | +0.86% |
| NXPC/USDT:USDT | below_1h_threshold | +0.68% | +0.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
