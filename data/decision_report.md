# Decision Report

- generated_at: 2026-07-16T18:16:27.894471+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8818**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8818, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.94% | **+0.78%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.12% | **+0.67%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.41% | **+0.99%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.46% | **+0.95%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.42% | **+0.88%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +5.40% | **+0.54%** |

## 2. $100 Live Portfolio

- 残高: **$109.89** / 初期 $100.00 (+9.89%)
- 確定トレード: 107件 (TP 40 / SL 64 / EXP 3)
- 最新: ALLO/USDT:USDT EXPIRED PnL +6.44% 残高後 $109.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.03** / 初期 $100.00 (+242.03%)
- 確定: 2933件 (Win 915 / Loss 945 / Flat 1073) / skip 2446件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ANSEM/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $342.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$107.06** / 初期 $100.00 (+7.06%)
- 確定: 780件 (Win 181 / Loss 171 / Flat 428) / skip 1449件
- 成長率目線: 平均log +0.000087 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0606 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ANSEM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $107.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.25** / 初期 $100.00 (-2.75%)
- 確定: 86件 (Win 24 / Loss 58 / Flat 4) / pending 4件 / skip 200件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $97.25

## 6. Latest Market Context

- 更新: 2026-07-16T18:16:17.244575+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=64126.0
- Funnel: target 880 → liquid 170 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ANSEM/USDT:USDT | +13.37% | $4,766,890.12 |
| TAC/USDT:USDT | +10.83% | $1,370,163.00 |
| CRO/USDT:USDT | +10.72% | $2,165,366.86 |
| SKYAI/USDT:USDT | +5.76% | $3,321,877.10 |
| SLX/USDT:USDT | +4.52% | $1,501,282.63 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRO/USDT:USDT | below_1h_threshold | +2.60% | +2.47% |
| MYX/USDT:USDT | below_1h_threshold | +2.07% | +1.95% |
| H/USDT:USDT | below_1h_threshold | +0.91% | +0.79% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.90% | +0.78% |
| DODO/USDT:USDT | below_1h_threshold | +0.90% | +0.77% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
