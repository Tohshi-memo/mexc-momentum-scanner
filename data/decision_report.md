# Decision Report

- generated_at: 2026-09-25T14:41:38.575938+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15533, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.74% | **-1.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +1.72% | **+1.21%** |
| LIMIT_5PCT | 4/20 | 20.0% | +4.48% | **+0.90%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.43% | **+0.37%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.96% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.11% | **+0.89%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.24% | **+0.81%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.14% | **+0.57%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.75% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 221件 (TP 81 / SL 135 / EXP 5)
- 最新: SYN/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,200.90** / 初期 $100.00 (+1100.90%)
- 確定: 5902件 (Win 1740 / Loss 1891 / Flat 2271) / skip 6192件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,200.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3466件 (Win 952 / Loss 793 / Flat 1721) / skip 5478件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0248 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ENA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3833件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000190 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T14:41:24.129037+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=83730.9
- Funnel: target 1066 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +52.56% | $6,952,723.57 |
| BP/USDT:USDT | +28.92% | $1,079,551.47 |
| ARK/USDT:USDT | +24.85% | $2,326,866.84 |
| B3/USDT:USDT | +20.83% | $1,070,438.55 |
| NIL/USDT:USDT | +15.96% | $8,343,851.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MSFTSTOCK/USDT:USDT | below_1h_threshold | +3.51% | +3.70% |
| PHA/USDT:USDT | below_1h_threshold | +2.45% | +2.64% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.39% | +2.58% |
| BP/USDT:USDT | below_1h_threshold | +1.95% | +2.14% |
| NIL/USDT:USDT | below_1h_threshold | +1.86% | +2.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
