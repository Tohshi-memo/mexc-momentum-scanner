# Decision Report

- generated_at: 2026-10-01T21:16:38.217281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15944**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.66% / filled 20/20。**
- 全期間 MARKET基準: n=15944, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.66%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.66% | **+0.66%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +6.27% | **+1.88%** |
| LIMIT_6PCT | 6/20 | 30.0% | +4.94% | **+1.48%** |
| LIMIT_ATR | 10/20 | 50.0% | +2.53% | **+1.27%** |
| LIMIT_8PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +2.90% | **+2.90%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.96% | **+1.66%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.79% | **+1.34%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,310.40** / 初期 $100.00 (+1210.40%)
- 確定: 6052件 (Win 1795 / Loss 1954 / Flat 2303) / skip 6453件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SI/USDT:USDT `LIMIT_7PCT` TP_HIT account +1.00% 残高後 $1,310.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$279.81** / 初期 $100.00 (+179.81%)
- 確定: 3597件 (Win 1004 / Loss 838 / Flat 1755) / skip 5758件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1118 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $279.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4111件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T21:16:22.474101+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=84545.5
- Funnel: target 1097 → liquid 172 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +73.78% | $2,407,990.24 |
| MAGMA/USDT:USDT | +19.90% | $1,390,663.85 |
| SI/USDT:USDT | +18.33% | $5,022,701.52 |
| LONGXIA/USDT:USDT | +10.79% | $11,748,897.53 |
| UAI/USDT:USDT | +9.91% | $1,856,937.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +2.96% | +3.01% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.36% | +1.41% |
| HNT/USDT:USDT | below_1h_threshold | +0.85% | +0.90% |
| LSK/USDT:USDT | below_1h_threshold | +0.78% | +0.83% |
| GRAM/USDT:USDT | below_1h_threshold | +0.70% | +0.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
