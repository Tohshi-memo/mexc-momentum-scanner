# Decision Report

- generated_at: 2026-09-02T18:46:39.347766+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13368**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13368, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.81% | **-2.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +6.00% | **+1.80%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_7PCT | 7/20 | 35.0% | +3.09% | **+1.08%** |
| LIMIT_10PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.77% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +6.00% | **+6.00%** |
| MARKET_LONG | 20/20 | 100.0% | +3.01% | **+3.01%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.15% | **+2.52%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.38% | **+2.03%** |
| LIMIT_4PCT_LONG | 5/20 | 25.0% | +3.22% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$879.05** / 初期 $100.00 (+779.05%)
- 確定: 4985件 (Win 1512 / Loss 1632 / Flat 1841) / skip 4944件
- 成長率目線: 平均log +0.000436 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $879.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$186.08** / 初期 $100.00 (+86.08%)
- 確定: 2347件 (Win 662 / Loss 562 / Flat 1123) / skip 4432件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1759 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $186.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2750件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000457 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T18:46:22.704739+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=77297.8
- Funnel: target 1044 → liquid 162 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 89.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +65.16% | $27,531,355.13 |
| FONE/USDT:USDT | +21.03% | $2,059,147.43 |
| BONER/USDT:USDT | +15.73% | $2,934,465.13 |
| BULLA/USDT:USDT | +8.91% | $1,895,844.40 |
| MARSCOIN/USDT:USDT | +8.62% | $3,104,060.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BULLA/USDT:USDT | below_1h_threshold | +3.96% | +4.03% |
| PONS/USDT:USDT | below_1h_threshold | +2.46% | +2.52% |
| OP/USDT:USDT | below_1h_threshold | +1.95% | +2.02% |
| EGLD/USDT:USDT | below_1h_threshold | +1.52% | +1.59% |
| ARB/USDT:USDT | below_1h_threshold | +1.51% | +1.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
