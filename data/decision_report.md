# Decision Report

- generated_at: 2026-10-02T07:26:33.037572+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15979**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15979, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.37% | **+0.96%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.27% | **+0.91%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.78% | **+0.62%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.46% | **+0.44%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.55% | **+0.28%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.21% | **+0.15%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.16% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$120.51** / 初期 $100.00 (+20.51%)
- 確定トレード: 227件 (TP 82 / SL 138 / EXP 7)
- 最新: BATON/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.51
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,311.39** / 初期 $100.00 (+1211.39%)
- 確定: 6084件 (Win 1802 / Loss 1957 / Flat 2325) / skip 6456件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAND/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,311.39

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3604件 (Win 1005 / Loss 844 / Flat 1755) / skip 5786件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0206 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4140件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T07:26:17.678669+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=85918.8
- Funnel: target 1098 → liquid 171 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.4 >= 65=1, 4h RSI n/a=1, 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +82.24% | $3,738,947.57 |
| MAGMA/USDT:USDT | +30.64% | $2,060,326.76 |
| SAND/USDT:USDT | +29.05% | $4,241,405.50 |
| CT/USDT:USDT | +20.57% | $7,362,150.81 |
| UAI/USDT:USDT | +12.78% | $2,945,266.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GALA/USDT:USDT | below_1h_threshold | +4.47% | +4.51% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.44% | +3.47% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +2.14% | +2.18% |
| KORU/USDT:USDT | below_1h_threshold | +0.97% | +1.01% |
| OP/USDT:USDT | below_1h_threshold | +0.96% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
