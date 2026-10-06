# Decision Report

- generated_at: 2026-10-06T14:06:37.735922+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16219**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16219, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_BB3S | 8/14 | 57.1% | +0.64% | **+0.37%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.44% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +2.67% | **+0.80%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.91% | **+0.67%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.95% | **+0.58%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.49% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$120.39** / 初期 $100.00 (+20.39%)
- 確定トレード: 231件 (TP 83 / SL 141 / EXP 7)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.39
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,349.38** / 初期 $100.00 (+1249.38%)
- 確定: 6260件 (Win 1840 / Loss 2002 / Flat 2418) / skip 6520件
- 成長率目線: 平均log +0.000416 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NMR/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,349.38

## 4. Robust Adaptive DryRun ($100)

- 残高: **$276.94** / 初期 $100.00 (+176.94%)
- 確定: 3627件 (Win 1010 / Loss 850 / Flat 1767) / skip 6003件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0260 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NMR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $276.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4382件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000286 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T14:06:23.343440+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=86181.5
- Funnel: target 1074 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.6 >= 65=1, 4h RSI 82.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +55.56% | $41,105,775.25 |
| BR/USDT:USDT | +53.71% | $53,868,809.14 |
| NMR/USDT:USDT | +39.43% | $9,261,112.35 |
| US/USDT:USDT | +36.81% | $1,393,059.45 |
| ORCA/USDT:USDT | +29.68% | $3,699,733.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.39% | +4.50% |
| NMR/USDT:USDT | below_1h_threshold | +3.00% | +3.11% |
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +2.48% | +2.58% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.65% | +1.76% |
| TRB/USDT:USDT | below_1h_threshold | +1.00% | +1.11% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
