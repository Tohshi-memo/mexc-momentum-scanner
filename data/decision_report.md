# Decision Report

- generated_at: 2026-07-20T14:41:24.489570+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9116**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9116, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_BB3S | 5/14 | 35.7% | +0.48% | **+0.17%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +1.76% | **+1.18%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.44% | **+0.57%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.43% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$402.42** / 初期 $100.00 (+302.42%)
- 確定: 3178件 (Win 993 / Loss 1009 / Flat 1176) / skip 2499件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $402.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.06** / 初期 $100.00 (+27.06%)
- 確定: 1077件 (Win 280 / Loss 219 / Flat 578) / skip 1450件
- 成長率目線: 平均log +0.000222 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0561 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PROM/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $127.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.16** / 初期 $100.00 (+1.16%)
- 確定: 315件 (Win 107 / Loss 139 / Flat 69) / pending 6件 / skip 268件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PROM/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.16

## 6. Latest Market Context

- 更新: 2026-07-20T14:41:15.025154+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64392.0
- Funnel: target 887 → liquid 152 → pre 50 → checked 49 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=45, below_relative_strength=1, invalid_ohlcv=0, errors=1
- Strict後reject: 4h RSI 95.6 >= 65=1, 4h RSI 73.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +88.29% | $27,664,450.54 |
| BANK/USDT:USDT | +78.27% | $126,880,806.34 |
| PROM/USDT:USDT | +65.42% | $7,326,783.52 |
| EVAA/USDT:USDT | +27.10% | $8,086,031.31 |
| PUMPFUN/USDT:USDT | +17.36% | $39,192,920.32 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_relative_strength | +5.08% | +4.96% |
| EVAA/USDT:USDT | below_1h_threshold | +3.62% | +3.49% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +2.91% | +2.78% |
| ON/USDT:USDT | below_1h_threshold | +2.51% | +2.39% |
| KORU/USDT:USDT | below_1h_threshold | +1.68% | +1.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
