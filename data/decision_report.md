# Decision Report

- generated_at: 2026-09-29T20:21:32.062834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15795**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15795, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_8PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.85% | **+0.55%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.24% | **+0.49%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.07%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.09% | **+1.88%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.14% | **+1.09%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.67% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5987件 (Win 1766 / Loss 1925 / Flat 2296) / skip 6369件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GRASS/USDT:USDT `LIMIT_BB3S` EXPIRED account +0.00% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3535件 (Win 974 / Loss 812 / Flat 1749) / skip 5671件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0411 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3959件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-29T20:21:18.493684+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=83597.1
- Funnel: target 1073 → liquid 164 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +110.56% | $2,598,057.22 |
| GRASS/USDT:USDT | +8.98% | $10,756,656.76 |
| QNT/USDT:USDT | +7.16% | $331,089,458.52 |
| NIL/USDT:USDT | +6.19% | $2,532,379.61 |
| SOONNETWORK/USDT:USDT | +5.21% | $2,892,475.49 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +2.17% | +2.12% |
| LDO/USDT:USDT | below_1h_threshold | +1.88% | +1.83% |
| ICP/USDT:USDT | below_1h_threshold | +1.84% | +1.80% |
| NIL/USDT:USDT | below_1h_threshold | +1.54% | +1.49% |
| SAND/USDT:USDT | below_1h_threshold | +1.51% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
