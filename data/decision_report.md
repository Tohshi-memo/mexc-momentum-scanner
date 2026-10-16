# Decision Report

- generated_at: 2026-10-16T08:16:23.120060+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16786**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=16786, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.57% | **+1.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.39% | **+1.08%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.09% | **+0.87%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.10% | **+0.78%** |
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.49% | **+1.50%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.95% | **+0.57%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +0.72% | **+0.51%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +3.32% | **+0.50%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.54% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 241件 (TP 89 / SL 145 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,254.65** / 初期 $100.00 (+1154.65%)
- 確定: 6315件 (Win 1849 / Loss 2027 / Flat 2439) / skip 7032件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,254.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.93** / 初期 $100.00 (+175.93%)
- 確定: 3678件 (Win 1025 / Loss 873 / Flat 1780) / skip 6519件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0205 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TIA/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $275.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4946件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-16T08:16:11.414953+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=82200.0
- Funnel: target 1078 → liquid 181 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +72.57% | $8,462,054.50 |
| CLAUDIA/USDT:USDT | +26.57% | $1,005,780.18 |
| ICNT/USDT:USDT | +18.36% | $1,203,371.92 |
| STBL/USDT:USDT | +16.85% | $1,521,296.03 |
| INJ/USDT:USDT | +15.04% | $75,904,624.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLAUDIA/USDT:USDT | below_1h_threshold | +2.01% | +2.08% |
| ALGO/USDT:USDT | below_1h_threshold | +1.34% | +1.41% |
| DASH/USDT:USDT | below_1h_threshold | +0.80% | +0.87% |
| CT/USDT:USDT | below_1h_threshold | +0.74% | +0.81% |
| SI/USDT:USDT | below_1h_threshold | +0.59% | +0.66% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
