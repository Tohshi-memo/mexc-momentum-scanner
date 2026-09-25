# Decision Report

- generated_at: 2026-09-25T12:31:24.504517+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15527**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15527, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.32%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.32% | **-1.32%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.82% | **+1.46%** |
| LIMIT_5PCT | 7/20 | 35.0% | +3.97% | **+1.39%** |
| LIMIT_4PCT | 14/20 | 70.0% | +1.71% | **+1.20%** |
| LIMIT_ATR | 17/20 | 85.0% | +1.23% | **+1.05%** |
| LIMIT_6PCT | 3/20 | 15.0% | +5.96% | **+0.89%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.92% | **+0.96%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.64% | **+0.82%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.72% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$120.32** / 初期 $100.00 (+20.32%)
- 確定トレード: 220件 (TP 80 / SL 135 / EXP 5)
- 最新: MYX/USDT:USDT TP_HIT PnL +7.62% 残高後 $120.32
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,200.90** / 初期 $100.00 (+1100.90%)
- 確定: 5902件 (Win 1740 / Loss 1891 / Flat 2271) / skip 6186件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,200.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3460件 (Win 952 / Loss 793 / Flat 1715) / skip 5478件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PHA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3830件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T12:31:13.048242+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.08% price=84463.5
- Funnel: target 1069 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHA/USDT:USDT | +35.96% | $3,639,479.42 |
| BP/USDT:USDT | +34.24% | $1,030,513.97 |
| ARK/USDT:USDT | +30.08% | $2,054,825.47 |
| B3/USDT:USDT | +20.03% | $1,033,893.27 |
| QNT/USDT:USDT | +17.37% | $15,975,108.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +1.55% | +1.63% |
| XRP/USDT:USDT | below_1h_threshold | +1.41% | +1.49% |
| TAO/USDT:USDT | below_1h_threshold | +1.33% | +1.42% |
| ONDO/USDT:USDT | below_1h_threshold | +1.24% | +1.33% |
| BTW/USDT:USDT | below_1h_threshold | +1.17% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
