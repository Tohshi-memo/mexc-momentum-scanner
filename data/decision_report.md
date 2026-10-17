# Decision Report

- generated_at: 2026-10-17T11:51:35.941582+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16871**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.51% / filled 20/20。**
- 全期間 MARKET基準: n=16871, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.51%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.51% | **+2.51%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.51% | **+2.51%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.02% | **+1.71%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.95% | **+1.17%** |
| LIMIT_ATR | 8/20 | 40.0% | +2.63% | **+1.05%** |
| LIMIT_3PCT | 9/20 | 45.0% | +1.35% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.37% | **+0.24%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.44% | **+0.20%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -2.29% | **-0.23%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 244件 (TP 91 / SL 146 / EXP 7)
- 最新: CLAUDIA/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,271.71** / 初期 $100.00 (+1171.71%)
- 確定: 6345件 (Win 1855 / Loss 2032 / Flat 2458) / skip 7087件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAND/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $1,271.71

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.05** / 初期 $100.00 (+174.05%)
- 確定: 3689件 (Win 1027 / Loss 878 / Flat 1784) / skip 6593件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0550 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5034件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-17T11:51:14.319724+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=81555.2
- Funnel: target 1084 → liquid 159 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +92.23% | $19,789,596.77 |
| EPIC/USDT:USDT | +28.15% | $1,298,215.08 |
| SIREN/USDT:USDT | +14.40% | $2,481,858.00 |
| ICNT/USDT:USDT | +14.13% | $8,890,294.44 |
| SAND/USDT:USDT | +12.95% | $8,501,384.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAND/USDT:USDT | below_1h_threshold | +4.49% | +4.56% |
| BTW/USDT:USDT | below_1h_threshold | +3.26% | +3.33% |
| NIL/USDT:USDT | below_1h_threshold | +1.80% | +1.87% |
| AGT/USDT:USDT | below_1h_threshold | +1.62% | +1.69% |
| NMR/USDT:USDT | below_1h_threshold | +1.15% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
