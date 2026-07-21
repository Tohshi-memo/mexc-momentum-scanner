# Decision Report

- generated_at: 2026-07-21T01:06:12.690196+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9135**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9135, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.56%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.56% | **-0.56%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.16% | **+0.15%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.03% | **+0.02%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.36% | **+0.95%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.93% | **+0.84%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.39% | **+0.83%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +8.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.43** / 初期 $100.00 (+304.43%)
- 確定: 3197件 (Win 1000 / Loss 1016 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000437 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $404.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.75** / 初期 $100.00 (+27.75%)
- 確定: 1096件 (Win 286 / Loss 224 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1146 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ON/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $127.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.81** / 初期 $100.00 (+1.81%)
- 確定: 332件 (Win 118 / Loss 145 / Flat 69) / pending 5件 / skip 272件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000363 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ON/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.81

## 6. Latest Market Context

- 更新: 2026-07-21T01:06:06.094133+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=65497.5
- Funnel: target 885 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +41.95% | $2,690,674.64 |
| HEMI/USDT:USDT | +21.67% | $2,991,167.08 |
| LDO/USDT:USDT | +9.14% | $5,798,521.06 |
| ESPORTS/USDT:USDT | +8.71% | $7,133,736.46 |
| BLESS/USDT:USDT | +8.06% | $1,511,821.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +1.30% | +1.37% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.01% | +1.08% |
| SYN/USDT:USDT | below_1h_threshold | +0.97% | +1.04% |
| IRENSTOCK/USDT:USDT | below_1h_threshold | +0.80% | +0.87% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.52% | +0.59% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
