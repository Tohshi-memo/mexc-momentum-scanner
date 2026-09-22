# Decision Report

- generated_at: 2026-09-22T08:36:21.183100+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15308**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15308, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 9/17 | 52.9% | +3.35% | **+1.77%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.78% | **+0.70%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_5PCT | 3/20 | 15.0% | +3.30% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.94% | **+0.85%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.31% | **+0.52%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.61% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,175.15** / 初期 $100.00 (+1075.15%)
- 確定: 5799件 (Win 1724 / Loss 1868 / Flat 2207) / skip 6070件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,175.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$248.25** / 初期 $100.00 (+148.25%)
- 確定: 3347件 (Win 924 / Loss 779 / Flat 1644) / skip 5372件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $248.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.65** / 初期 $100.00 (+22.65%)
- 確定: 3080件 (Win 905 / Loss 1206 / Flat 969) / pending 4件 / skip 3695件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000166 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.65

## 6. Latest Market Context

- 更新: 2026-09-22T08:36:09.960276+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=85594.0
- Funnel: target 1056 → liquid 187 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +57.07% | $1,133,482.82 |
| KERNEL/USDT:USDT | +36.64% | $4,038,630.54 |
| 4STOCK/USDT:USDT | +36.51% | $1,839,064.55 |
| MUBARAK/USDT:USDT | +23.21% | $2,992,552.45 |
| GRASS/USDT:USDT | +21.00% | $3,189,793.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.94% | +3.62% |
| AGT/USDT:USDT | below_1h_threshold | +3.13% | +2.81% |
| 4STOCK/USDT:USDT | below_1h_threshold | +3.06% | +2.75% |
| FET/USDT:USDT | below_1h_threshold | +1.78% | +1.47% |
| WIF/USDT:USDT | below_1h_threshold | +1.73% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
