# Decision Report

- generated_at: 2026-08-05T06:31:28.515170+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10373**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10373, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.97% | **-0.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.18% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/8 | 87.5% | +3.56% | **+3.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.06% | **+1.85%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.78% | **+1.67%** |
| MARKET_LONG | 20/20 | 100.0% | +1.44% | **+1.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.93% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$623.79** / 初期 $100.00 (+523.79%)
- 確定: 3763件 (Win 1195 / Loss 1230 / Flat 1338) / skip 3171件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $623.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$145.05** / 初期 $100.00 (+45.05%)
- 確定: 1307件 (Win 369 / Loss 304 / Flat 634) / skip 2477件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $145.05

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.21** / 初期 $100.00 (+19.21%)
- 確定: 1122件 (Win 361 / Loss 431 / Flat 330) / pending 4件 / skip 720件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000415 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.21

## 6. Latest Market Context

- 更新: 2026-08-05T06:31:17.212347+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=64279.8
- Funnel: target 939 → liquid 181 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +83.29% | $12,882,791.45 |
| HFT/USDT:USDT | +64.73% | $1,613,273.87 |
| BLESS/USDT:USDT | +54.93% | $26,062,637.25 |
| BICO/USDT:USDT | +49.42% | $16,370,929.07 |
| SYN/USDT:USDT | +32.29% | $2,551,888.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HFT/USDT:USDT | below_1h_threshold | +4.76% | +4.81% |
| SNXX/USDT:USDT | below_1h_threshold | +3.16% | +3.20% |
| BEAT/USDT:USDT | below_1h_threshold | +2.59% | +2.63% |
| MUU/USDT:USDT | below_1h_threshold | +2.50% | +2.54% |
| ALLO/USDT:USDT | below_1h_threshold | +2.44% | +2.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
