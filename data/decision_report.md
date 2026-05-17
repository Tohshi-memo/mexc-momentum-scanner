# Decision Report

- generated_at: 2026-05-17T10:05:08.788575+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4395**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4395, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.50%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.50% | **-0.50%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +2.35% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 11/19 | 57.9% | -0.23% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.08% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.29% | **+0.77%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.27% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$96.71** / 初期 $100.00 (-3.29%)
- 確定トレード: 51件 (TP 13 / SL 35 / EXP 3)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$117.96** / 初期 $100.00 (+17.96%)
- 確定: 395件 (Win 99 / Loss 137 / Flat 159) / skip 561件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +4.21%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $117.96

## 4. Latest Market Context

- 更新: 2026-05-17T10:05:06.818266+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=78304.1
- Funnel: target 760 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +29.37% | $6,016,236.41 |
| CGPT/USDT:USDT | +24.03% | $2,127,878.59 |
| ASTEROID/USDT:USDT | +17.52% | $4,274,865.72 |
| AIA/USDT:USDT | +15.27% | $12,261,338.37 |
| VVV/USDT:USDT | +9.23% | $5,804,760.80 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CGPT/USDT:USDT | below_1h_threshold | +2.84% | +2.72% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.52% | +1.41% |
| BEAT/USDT:USDT | below_1h_threshold | +0.82% | +0.71% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.74% | +0.62% |
| DASH/USDT:USDT | below_1h_threshold | +0.71% | +0.60% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
