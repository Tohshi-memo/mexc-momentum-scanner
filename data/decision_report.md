# Decision Report

- generated_at: 2026-11-15T01:21:23.853506+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18925**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18925, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.51% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.78%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.21% | **+0.72%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.43% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 275件 (TP 99 / SL 168 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,746.38** / 初期 $100.00 (+1646.38%)
- 確定: 7329件 (Win 2106 / Loss 2344 / Flat 2879) / skip 8157件
- 成長率目線: 平均log +0.000390 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SOPH/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,746.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$428.00** / 初期 $100.00 (+328.00%)
- 確定: 4933件 (Win 1320 / Loss 1080 / Flat 2533) / skip 7403件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0673 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOPH/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $428.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7086件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000297 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-15T01:21:09.031563+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.85% price=62861.0
- Funnel: target 1071 → liquid 134 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +35.72% | $3,983,729.61 |
| SHELL/USDT:USDT | +9.89% | $2,365,138.73 |
| JCT/USDT:USDT | +7.34% | $5,022,970.26 |
| ARIA/USDT:USDT | +6.89% | $2,327,400.89 |
| BTW/USDT:USDT | +3.94% | $5,059,444.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARIA/USDT:USDT | below_1h_threshold | +2.23% | +3.09% |
| AGT/USDT:USDT | below_1h_threshold | +1.77% | +2.62% |
| BLESS/USDT:USDT | below_1h_threshold | +1.62% | +2.47% |
| DODO/USDT:USDT | below_1h_threshold | +0.97% | +1.82% |
| BTW/USDT:USDT | below_1h_threshold | +0.96% | +1.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
