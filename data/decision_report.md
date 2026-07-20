# Decision Report

- generated_at: 2026-07-20T13:26:23.287918+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9109**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9109, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.55% | **+1.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.23% | **+0.55%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.50% | **+0.28%** |
| LIMIT_BB3S | 6/16 | 37.5% | +0.51% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +7.03% | **+5.27%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.84% | **+1.57%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$403.40** / 初期 $100.00 (+303.40%)
- 確定: 3171件 (Win 991 / Loss 1006 / Flat 1174) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $403.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$126.87** / 初期 $100.00 (+26.87%)
- 確定: 1070件 (Win 279 / Loss 219 / Flat 572) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0589 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $126.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.35** / 初期 $100.00 (+1.35%)
- 確定: 308件 (Win 104 / Loss 135 / Flat 69) / pending 4件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $101.35

## 6. Latest Market Context

- 更新: 2026-07-20T13:26:15.590411+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=64544.9
- Funnel: target 887 → liquid 144 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.9 >= 65=1, 4h RSI 67.4 >= 65=1, 4h RSI 74.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +87.68% | $24,629,931.77 |
| BANK/USDT:USDT | +71.77% | $122,192,866.48 |
| PROM/USDT:USDT | +55.49% | $4,841,539.27 |
| EVAA/USDT:USDT | +19.80% | $7,726,203.70 |
| PUMPFUN/USDT:USDT | +16.16% | $36,520,969.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +2.14% | +2.27% |
| BEAT/USDT:USDT | below_1h_threshold | +1.44% | +1.57% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.22% | +1.34% |
| PI/USDT:USDT | below_1h_threshold | +0.95% | +1.08% |
| CHZ/USDT:USDT | below_1h_threshold | +0.92% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
