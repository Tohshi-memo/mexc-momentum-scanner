# Decision Report

- generated_at: 2026-07-16T17:01:12.340122+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8814**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8814, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.74% | **-0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.82% | **+0.41%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_9PCT | 2/20 | 10.0% | +0.29% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.84% | **+1.84%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +1.75% | **+1.14%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.82% | **+1.09%** |
| LIMIT_8PCT_LONG | 4/20 | 20.0% | +4.42% | **+0.88%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.97% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$109.89** / 初期 $100.00 (+9.89%)
- 確定トレード: 107件 (TP 40 / SL 64 / EXP 3)
- 最新: ALLO/USDT:USDT EXPIRED PnL +6.44% 残高後 $109.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$341.23** / 初期 $100.00 (+241.23%)
- 確定: 2929件 (Win 914 / Loss 945 / Flat 1070) / skip 2446件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $341.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.90** / 初期 $100.00 (+6.90%)
- 確定: 776件 (Win 180 / Loss 171 / Flat 425) / skip 1449件
- 成長率目線: 平均log +0.000086 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0515 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $106.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$97.26** / 初期 $100.00 (-2.74%)
- 確定: 83件 (Win 23 / Loss 56 / Flat 4) / pending 3件 / skip 198件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000207 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $97.26

## 6. Latest Market Context

- 更新: 2026-07-16T17:01:06.125138+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=64420.5
- Funnel: target 880 → liquid 167 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DODO/USDT:USDT | +5.19% | $4,853,726.56 |
| BSB/USDT:USDT | +3.22% | $3,880,968.38 |
| US/USDT:USDT | +3.03% | $15,607,924.71 |
| ROAM/USDT:USDT | +2.34% | $6,278,485.15 |
| IBMSTOCK/USDT:USDT | +1.98% | $3,384,193.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IBMSTOCK/USDT:USDT | below_1h_threshold | +2.24% | +2.29% |
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |
| AEHRSTOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.64% |
| BANK/USDT:USDT | below_1h_threshold | +0.58% | +0.63% |
| ESPORTS/USDT:USDT | below_1h_threshold | +0.53% | +0.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
