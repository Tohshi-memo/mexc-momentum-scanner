# Decision Report

- generated_at: 2026-08-30T00:21:34.391040+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12978**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12978, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.40% | **-1.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +4.57% | **+1.37%** |
| LIMIT_9PCT | 5/20 | 25.0% | +4.92% | **+1.23%** |
| LIMIT_7PCT | 10/20 | 50.0% | +2.32% | **+1.16%** |
| LIMIT_10PCT | 4/20 | 20.0% | +4.36% | **+0.87%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.72% | **+0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +3.74% | **+3.00%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.27% | **+2.94%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +3.34% | **+2.34%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.79% | **+1.39%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$777.27** / 初期 $100.00 (+677.27%)
- 確定: 4748件 (Win 1446 / Loss 1559 / Flat 1743) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $777.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.21** / 初期 $100.00 (+71.21%)
- 確定: 2062件 (Win 573 / Loss 495 / Flat 994) / skip 4327件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1924 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $171.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2413件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000491 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-30T00:21:21.446772+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=78212.1
- Funnel: target 1023 → liquid 118 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FONE/USDT:USDT | +46.96% | $1,278,480.95 |
| PROM/USDT:USDT | +28.82% | $10,109,579.84 |
| PONS/USDT:USDT | +21.23% | $1,182,024.31 |
| HNT/USDT:USDT | +20.60% | $23,517,109.31 |
| BTR/USDT:USDT | +20.57% | $9,863,159.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +2.50% | +2.48% |
| PROM/USDT:USDT | below_1h_threshold | +2.45% | +2.44% |
| PONS/USDT:USDT | below_1h_threshold | +2.34% | +2.33% |
| O/USDT:USDT | below_1h_threshold | +1.68% | +1.66% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.60% | +1.58% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
