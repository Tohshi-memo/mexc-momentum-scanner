# Decision Report

- generated_at: 2026-08-08T19:51:42.640040+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10881**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.30% / filled 20/20。**
- 全期間 MARKET基準: n=10881, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.30% | **+1.30%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.95% | **+0.86%** |
| LIMIT_BB3S | 3/17 | 17.6% | +2.86% | **+0.50%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.70% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +6.07% | **+0.91%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.60% | **+0.30%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.56% | **+0.23%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +0.38% | **+0.19%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$645.93** / 初期 $100.00 (+545.93%)
- 確定: 3882件 (Win 1223 / Loss 1264 / Flat 1395) / skip 3560件
- 成長率目線: 平均log +0.000481 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $645.93

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2781件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0840 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.93** / 初期 $100.00 (+17.93%)
- 確定: 1241件 (Win 389 / Loss 477 / Flat 375) / pending 6件 / skip 1111件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000140 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $117.93

## 6. Latest Market Context

- 更新: 2026-08-08T19:51:26.204910+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=65026.9
- Funnel: target 961 → liquid 154 → pre 50 → checked 50 → surge 4 → strict 3
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLUAI/USDT:USDT | +25.39% | $6,121,309.97 |
| COOKIE/USDT:USDT | +19.60% | $1,381,243.29 |
| CATI/USDT:USDT | +14.53% | $1,833,124.48 |
| CYS/USDT:USDT | +14.21% | $31,026,112.56 |
| LIGHT/USDT:USDT | +12.60% | $1,235,888.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.52% | +4.50% |
| ACE/USDT:USDT | below_1h_threshold | +3.99% | +3.97% |
| CYS/USDT:USDT | below_1h_threshold | +3.57% | +3.55% |
| ALLO/USDT:USDT | below_1h_threshold | +3.12% | +3.10% |
| GIGGLE/USDT:USDT | below_1h_threshold | +2.85% | +2.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
