# Decision Report

- generated_at: 2026-07-16T18:46:26.320263+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8819**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8819, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.07% | **+0.73%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.62%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.84% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.78% | **+0.87%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.10% | **+0.83%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.12% | **+0.78%** |

## 2. $100 Live Portfolio

- 残高: **$109.89** / 初期 $100.00 (+9.89%)
- 確定トレード: 107件 (TP 40 / SL 64 / EXP 3)
- 最新: ALLO/USDT:USDT EXPIRED PnL +6.44% 残高後 $109.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$345.45** / 初期 $100.00 (+245.45%)
- 確定: 2934件 (Win 916 / Loss 945 / Flat 1073) / skip 2446件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CRO/USDT:USDT `LIMIT_8PCT_LONG` TP_HIT account +1.00% 残高後 $345.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 781件 (Win 181 / Loss 171 / Flat 429) / skip 1449件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0606 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CRO/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.25** / 初期 $100.00 (-2.75%)
- 確定: 86件 (Win 24 / Loss 58 / Flat 4) / pending 5件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $97.25

## 6. Latest Market Context

- 更新: 2026-07-16T18:46:14.825785+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=64154.7
- Funnel: target 880 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +9.14% | $5,050,249.26 |
| TAC/USDT:USDT | +8.76% | $1,484,912.19 |
| SLX/USDT:USDT | +6.61% | $1,549,139.78 |
| KAITO/USDT:USDT | +6.09% | $1,133,482.46 |
| DEXE/USDT:USDT | +5.05% | $4,067,275.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +2.98% | +2.81% |
| KAITO/USDT:USDT | below_1h_threshold | +2.58% | +2.41% |
| SLX/USDT:USDT | below_1h_threshold | +2.51% | +2.34% |
| ALLO/USDT:USDT | below_1h_threshold | +2.21% | +2.04% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +1.94% | +1.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
