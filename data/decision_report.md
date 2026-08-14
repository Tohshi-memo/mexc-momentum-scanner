# Decision Report

- generated_at: 2026-08-14T23:06:29.897589+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11616**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11616, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.65%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.65% | **-0.65%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.48% | **+0.99%** |
| LIMIT_5PCT | 4/20 | 20.0% | +2.71% | **+0.54%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.85% | **+0.51%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.05% | **+1.54%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +0.95% | **+0.95%** |
| MARKET_LONG | 20/20 | 100.0% | +0.66% | **+0.66%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.75% | **+0.64%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.94% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$647.24** / 初期 $100.00 (+547.24%)
- 確定: 4084件 (Win 1281 / Loss 1343 / Flat 1460) / skip 4093件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEI/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $647.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.13** / 初期 $100.00 (+54.13%)
- 確定: 1679件 (Win 482 / Loss 405 / Flat 792) / skip 3348件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1029 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $154.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.15** / 初期 $100.00 (+18.15%)
- 確定: 1564件 (Win 477 / Loss 598 / Flat 489) / pending 2件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000337 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEI/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $118.15

## 6. Latest Market Context

- 更新: 2026-08-14T23:06:19.920930+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=62858.1
- Funnel: target 985 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +26.71% | $73,854,352.68 |
| US/USDT:USDT | +21.87% | $6,718,984.06 |
| HEI/USDT:USDT | +20.42% | $5,101,272.08 |
| DOLO/USDT:USDT | +12.14% | $1,641,027.20 |
| GUN/USDT:USDT | +11.85% | $1,010,037.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +0.83% | +0.83% |
| RE/USDT:USDT | below_1h_threshold | +0.82% | +0.82% |
| US/USDT:USDT | below_1h_threshold | +0.57% | +0.57% |
| 2Z/USDT:USDT | below_1h_threshold | +0.49% | +0.49% |
| EDEN/USDT:USDT | below_1h_threshold | +0.47% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
