# Decision Report

- generated_at: 2026-10-14T16:36:37.145138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16688**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16688, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_5PCT | 8/20 | 40.0% | -0.90% | **-0.36%** |
| LIMIT_6PCT | 5/20 | 25.0% | -1.65% | **-0.41%** |
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.04% | **+0.94%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.00% | **+0.75%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.08% | **+0.65%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.25% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,278.87** / 初期 $100.00 (+1178.87%)
- 確定: 6297件 (Win 1845 / Loss 2018 / Flat 2434) / skip 6952件
- 成長率目線: 平均log +0.000405 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_FIB1618_LONG` EXPIRED account +0.00% 残高後 $1,278.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.76** / 初期 $100.00 (+170.76%)
- 確定: 3654件 (Win 1015 / Loss 864 / Flat 1775) / skip 6445件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0160 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGIC/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.76

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4850件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000120 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-14T16:36:19.867699+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=81788.1
- Funnel: target 1085 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| WAL/USDT:USDT | +11.73% | $6,905,556.90 |
| CLAUDIA/USDT:USDT | +6.69% | $2,012,292.21 |
| DEEP/USDT:USDT | +4.11% | $1,520,050.43 |
| GRASS/USDT:USDT | +2.95% | $2,755,905.93 |
| 1000RATS/USDT:USDT | +2.11% | $3,115,302.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEEP/USDT:USDT | below_1h_threshold | +3.94% | +3.71% |
| SOXS/USDT:USDT | below_1h_threshold | +3.27% | +3.04% |
| GRASS/USDT:USDT | below_1h_threshold | +3.01% | +2.78% |
| 1000RATS/USDT:USDT | below_1h_threshold | +2.11% | +1.88% |
| AVA/USDT:USDT | below_1h_threshold | +2.09% | +1.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
