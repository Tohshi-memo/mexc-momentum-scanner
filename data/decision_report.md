# Decision Report

- generated_at: 2026-08-29T22:46:31.318390+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12971**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12971, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +0.99% | **+0.55%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.90% | **+0.36%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.62% | **+0.34%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.91% | **+2.48%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.33% | **+2.33%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.35% | **+2.17%** |
| MARKET_LONG | 20/20 | 100.0% | +1.41% | **+1.41%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.32% | **+0.23%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$756.70** / 初期 $100.00 (+656.70%)
- 確定: 4741件 (Win 1441 / Loss 1557 / Flat 1743) / skip 4791件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $756.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$168.12** / 初期 $100.00 (+68.12%)
- 確定: 2055件 (Win 568 / Loss 493 / Flat 994) / skip 4327件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1600 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $168.12

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2406件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000405 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T22:46:17.858772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=78161.4
- Funnel: target 1023 → liquid 120 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1, 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +28.50% | $1,238,110.70 |
| PROM/USDT:USDT | +26.16% | $9,117,353.01 |
| HNT/USDT:USDT | +23.11% | $21,260,624.75 |
| BTW/USDT:USDT | +19.18% | $3,465,348.99 |
| BTR/USDT:USDT | +14.82% | $9,837,889.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +4.62% | +4.58% |
| PONS/USDT:USDT | below_1h_threshold | +2.68% | +2.64% |
| ENA/USDT:USDT | below_1h_threshold | +2.32% | +2.28% |
| BTW/USDT:USDT | below_1h_threshold | +2.05% | +2.01% |
| 4/USDT:USDT | below_1h_threshold | +1.82% | +1.78% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
