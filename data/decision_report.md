# Decision Report

- generated_at: 2026-05-19T18:23:40.666554+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4492**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4492, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_7PCT | 6/20 | 30.0% | +1.40% | **+0.42%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.49% | **+0.27%** |
| LIMIT_5PCT | 11/20 | 55.0% | +0.24% | **+0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/9 | 44.4% | +5.24% | **+2.33%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.48% | **+1.11%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.81% | **+0.91%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定: 473件 (Win 124 / Loss 164 / Flat 185) / skip 580件
- 成長率目線: 平均log +0.000412 / 幾何平均 +0.041% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $121.49

## 4. Latest Market Context

- 更新: 2026-05-19T18:23:38.678291+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=76781.5
- Funnel: target 760 → liquid 135 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +47.25% | $14,658,379.67 |
| EDEN/USDT:USDT | +33.08% | $8,646,939.52 |
| VVV/USDT:USDT | +11.45% | $8,414,195.64 |
| PLAY/USDT:USDT | +7.90% | $8,247,663.39 |
| LIT/USDT:USDT | +7.68% | $1,934,698.87 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +1.12% | +1.17% |
| LAB/USDT:USDT | below_1h_threshold | +1.07% | +1.12% |
| BSB/USDT:USDT | below_1h_threshold | +0.94% | +0.99% |
| SIREN/USDT:USDT | below_1h_threshold | +0.78% | +0.83% |
| ETC/USDT:USDT | below_1h_threshold | +0.68% | +0.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
