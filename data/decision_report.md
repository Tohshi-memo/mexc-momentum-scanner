# Decision Report

- generated_at: 2026-09-09T08:51:30.011995+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14047**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.59% / filled 20/20。**
- 全期間 MARKET基準: n=14047, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 16/20 | 80.0% | +1.33% | **+1.07%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.88% | **+0.71%** |
| MARKET | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.81% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.23% | **+0.23%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | -0.30% | **-0.14%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | -0.21% | **-0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,001.94** / 初期 $100.00 (+901.94%)
- 確定: 5311件 (Win 1594 / Loss 1713 / Flat 2004) / skip 5297件
- 成長率目線: 平均log +0.000434 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CNPY/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $1,001.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.39** / 初期 $100.00 (+90.39%)
- 確定: 2650件 (Win 729 / Loss 623 / Flat 1298) / skip 4808件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0034 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $190.39

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.95** / 初期 $100.00 (+17.95%)
- 確定: 2619件 (Win 765 / Loss 1000 / Flat 854) / pending 1件 / skip 2899件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000206 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CRO/USDT:USDT `MARKET` EXPIRED account +0.11% 残高後 $117.95

## 6. Latest Market Context

- 更新: 2026-09-09T08:51:17.323540+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.40% price=79566.6
- Funnel: target 1064 → liquid 160 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +65.54% | $1,386,383.19 |
| IOST/USDT:USDT | +33.81% | $3,408,678.89 |
| CNPY/USDT:USDT | +24.57% | $1,096,892.31 |
| OL/USDT:USDT | +19.42% | $2,245,978.78 |
| RAY/USDT:USDT | +16.02% | $5,052,407.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IOST/USDT:USDT | below_1h_threshold | +4.83% | +4.43% |
| ATOM/USDT:USDT | below_1h_threshold | +4.08% | +3.68% |
| FF/USDT:USDT | below_1h_threshold | +3.52% | +3.12% |
| BULLA/USDT:USDT | below_1h_threshold | +3.50% | +3.09% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.20% | +2.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
