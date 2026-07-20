# Decision Report

- generated_at: 2026-07-20T17:56:22.647234+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9121**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9121, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.48% | **-0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.32% | **+1.19%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.58% | **+1.16%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.66% | **+0.91%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.76% | **+0.88%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$405.90** / 初期 $100.00 (+305.90%)
- 確定: 3183件 (Win 995 / Loss 1009 / Flat 1179) / skip 2499件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APDSTOCK/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.23% 残高後 $405.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.25** / 初期 $100.00 (+27.25%)
- 確定: 1082件 (Win 281 / Loss 219 / Flat 582) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1201 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APDSTOCK/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $127.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.85** / 初期 $100.00 (+1.85%)
- 確定: 320件 (Win 112 / Loss 139 / Flat 69) / pending 6件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APDSTOCK/USDT:USDT `MARKET_LONG` EXPIRED account +0.01% 残高後 $101.85

## 6. Latest Market Context

- 更新: 2026-07-20T17:56:16.065081+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=65531.9
- Funnel: target 885 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.0 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +6.28% | $27,640,655.79 |
| ALLO/USDT:USDT | +5.06% | $3,817,946.90 |
| ON/USDT:USDT | +4.96% | $1,407,785.57 |
| USELESS/USDT:USDT | +4.55% | $1,190,647.15 |
| UB/USDT:USDT | +4.51% | $1,119,841.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.96% | +4.88% |
| US/USDT:USDT | below_1h_threshold | +4.12% | +4.03% |
| USELESS/USDT:USDT | below_1h_threshold | +2.48% | +2.40% |
| RIVER/USDT:USDT | below_1h_threshold | +1.88% | +1.80% |
| ZRO/USDT:USDT | below_1h_threshold | +1.83% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
