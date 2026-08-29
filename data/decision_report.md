# Decision Report

- generated_at: 2026-08-29T20:56:22.542929+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12964**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12964, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.41%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.41% | **-0.41%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.38% | **+0.90%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_BB3S | 2/15 | 13.3% | +2.82% | **+0.38%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.49% | **+0.24%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.92% | **+2.33%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.19% | **+1.97%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.41% | **+1.57%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.21% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$753.03** / 初期 $100.00 (+653.03%)
- 確定: 4734件 (Win 1439 / Loss 1554 / Flat 1741) / skip 4791件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $753.03

## 4. Robust Adaptive DryRun ($100)

- 残高: **$165.87** / 初期 $100.00 (+65.87%)
- 確定: 2048件 (Win 565 / Loss 491 / Flat 992) / skip 4327件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1295 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $165.87

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2399件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T20:56:13.223708+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=78108.2
- Funnel: target 1023 → liquid 120 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +20.05% | $8,328,766.06 |
| HNT/USDT:USDT | +16.06% | $19,314,395.76 |
| BTW/USDT:USDT | +11.74% | $2,740,735.53 |
| BTR/USDT:USDT | +9.33% | $9,760,138.47 |
| FONE/USDT:USDT | +7.44% | $1,244,571.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 4/USDT:USDT | below_1h_threshold | +3.88% | +3.94% |
| CYS/USDT:USDT | below_1h_threshold | +3.80% | +3.86% |
| PONS/USDT:USDT | below_1h_threshold | +2.90% | +2.96% |
| COTI/USDT:USDT | below_1h_threshold | +1.96% | +2.02% |
| BTR/USDT:USDT | below_1h_threshold | +1.38% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
