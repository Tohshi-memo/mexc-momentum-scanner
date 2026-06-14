# Decision Report

- generated_at: 2026-06-14T17:08:33.180461+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6686**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6686, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.30%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.30% | **-0.30%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.88% | **+0.97%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.64% | **+0.82%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.82% | **+1.82%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.19% | **+0.36%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.99** / 初期 $100.00 (+0.99%)
- 確定トレード: 4件 (TP 2 / SL 2 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.99
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$175.51** / 初期 $100.00 (+75.51%)
- 確定: 1559件 (Win 417 / Loss 493 / Flat 649) / skip 1688件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $175.51

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.77** / 初期 $100.00 (-1.23%)
- 確定: 67件 (Win 19 / Loss 14 / Flat 34) / skip 30件
- 成長率目線: 平均log -0.000185 / 幾何平均 -0.019% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0361 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.20% 残高後 $98.77

## 5. Latest Market Context

- 更新: 2026-06-14T17:08:27.994198+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63893.4
- Funnel: target 770 → liquid 127 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +11.70% | $2,068,782.83 |
| STG/USDT:USDT | +5.97% | $6,455,315.04 |
| BANANAS31/USDT:USDT | +5.71% | $1,896,370.09 |
| CLO/USDT:USDT | +4.56% | $1,379,043.77 |
| MEGA/USDT:USDT | +3.78% | $4,934,136.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +1.87% | +1.91% |
| VELVET/USDT:USDT | below_1h_threshold | +1.71% | +1.74% |
| STG/USDT:USDT | below_1h_threshold | +1.60% | +1.64% |
| NOT/USDT:USDT | below_1h_threshold | +1.18% | +1.22% |
| ZEC/USDT:USDT | below_1h_threshold | +1.06% | +1.09% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
