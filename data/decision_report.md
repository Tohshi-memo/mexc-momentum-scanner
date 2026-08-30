# Decision Report

- generated_at: 2026-08-30T03:01:18.821832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12999**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12999, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 4/20 | 20.0% | +3.70% | **+0.74%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.47% | **+0.69%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.64% | **+0.61%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.67% | **+1.09%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$783.15** / 初期 $100.00 (+683.15%)
- 確定: 4769件 (Win 1454 / Loss 1569 / Flat 1746) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $783.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$171.94** / 初期 $100.00 (+71.94%)
- 確定: 2083件 (Win 581 / Loss 505 / Flat 997) / skip 4327件
- 成長率目線: 平均log +0.000260 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1206 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $171.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.04** / 初期 $100.00 (+16.04%)
- 確定: 2047件 (Win 601 / Loss 796 / Flat 650) / pending 5件 / skip 2424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000543 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MAGMA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.04

## 6. Latest Market Context

- 更新: 2026-08-30T03:01:09.485942+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=78072.2
- Funnel: target 1023 → liquid 115 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +64.46% | $1,564,528.11 |
| FONE/USDT:USDT | +41.40% | $1,259,196.47 |
| PROM/USDT:USDT | +38.46% | $13,033,763.21 |
| PONS/USDT:USDT | +35.54% | $1,372,524.69 |
| HNT/USDT:USDT | +28.97% | $26,332,949.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +2.01% | +2.01% |
| ZKP/USDT:USDT | below_1h_threshold | +0.66% | +0.66% |
| COTI/USDT:USDT | below_1h_threshold | +0.45% | +0.45% |
| KORU/USDT:USDT | below_1h_threshold | +0.42% | +0.42% |
| BLESS/USDT:USDT | below_1h_threshold | +0.37% | +0.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
