# Decision Report

- generated_at: 2026-06-20T09:58:13.574889+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7223**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7223, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.63% | **-1.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +3.73% | **+0.75%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.44% | **+0.49%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.01% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.45% | **+1.59%** |
| ASK_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.92% | **+1.46%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.64% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$101.96** / 初期 $100.00 (+1.96%)
- 確定トレード: 23件 (TP 9 / SL 14 / EXP 0)
- 最新: BLESS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.96
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$224.84** / 初期 $100.00 (+124.84%)
- 確定: 1970件 (Win 571 / Loss 641 / Flat 758) / skip 1814件
- 成長率目線: 平均log +0.000411 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $224.84

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 310件 (Win 89 / Loss 87 / Flat 134) / skip 324件
- 成長率目線: 平均log +0.000189 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-20T09:58:06.659719+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.50% price=63711.6
- Funnel: target 795 → liquid 145 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.0 >= 65=1, 4h RSI 82.7 >= 65=1, 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTW/USDT:USDT | +81.50% | $27,616,495.01 |
| BICO/USDT:USDT | +49.74% | $26,324,965.10 |
| BEL/USDT:USDT | +33.24% | $1,042,536.80 |
| GUA/USDT:USDT | +28.48% | $6,500,117.59 |
| AGT/USDT:USDT | +21.04% | $1,927,110.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.62% | +3.12% |
| AERO/USDT:USDT | below_1h_threshold | +2.57% | +2.06% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.46% | +1.95% |
| SAND/USDT:USDT | below_1h_threshold | +2.38% | +1.87% |
| MET/USDT:USDT | below_1h_threshold | +1.69% | +1.19% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
