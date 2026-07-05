# Decision Report

- generated_at: 2026-07-05T12:04:17.690930+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8322**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8322, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.19% | **+0.19%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.74% | **+0.44%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.09% | **+0.06%** |
| ASK_LONG | 20/20 | 100.0% | +0.04% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 64件 (TP 22 / SL 41 / EXP 1)
- 最新: HMSTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$323.56** / 初期 $100.00 (+223.56%)
- 確定: 2619件 (Win 832 / Loss 883 / Flat 904) / skip 2264件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `見送り` (no_strategy_passed_safety_filters) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $323.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.76** / 初期 $100.00 (+5.76%)
- 確定: 638件 (Win 152 / Loss 157 / Flat 329) / skip 1095件
- 成長率目線: 平均log +0.000088 / 幾何平均 +0.009% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HMSTR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $105.76

## 5. Latest Market Context

- 更新: 2026-07-05T12:04:11.544012+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=62558.4
- Funnel: target 835 → liquid 150 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NES/USDT:USDT | +30.91% | $3,019,600.56 |
| BTW/USDT:USDT | +23.01% | $4,082,618.00 |
| VANRY/USDT:USDT | +20.04% | $5,150,980.57 |
| HOT/USDT:USDT | +19.71% | $3,704,434.85 |
| CAP/USDT:USDT | +16.71% | $3,297,546.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VANRY/USDT:USDT | below_1h_threshold | +4.40% | +4.51% |
| XTZ/USDT:USDT | below_1h_threshold | +0.69% | +0.80% |
| MAGMA/USDT:USDT | below_1h_threshold | +0.40% | +0.51% |
| BTW/USDT:USDT | below_1h_threshold | +0.32% | +0.43% |
| WLFI/USDT:USDT | below_1h_threshold | +0.27% | +0.38% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
