# Decision Report

- generated_at: 2026-06-02T11:57:13.516959+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5449**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5449, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.92% | **+0.60%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |
| ASK | 20/20 | 100.0% | +0.28% | **+0.28%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.31% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +0.56% | **+0.11%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | -0.03% | **-0.02%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | -0.50% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 87件 (TP 25 / SL 59 / EXP 3)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$133.99** / 初期 $100.00 (+33.99%)
- 確定: 961件 (Win 226 / Loss 290 / Flat 445) / skip 1049件
- 成長率目線: 平均log +0.000305 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $133.99

## 4. Latest Market Context

- 更新: 2026-06-02T11:57:10.366111+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=69528.9
- Funnel: target 773 → liquid 154 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.9 >= 65=1, 4h RSI 73.8 >= 65=1, 4h RSI 73.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| US/USDT:USDT | +42.54% | $3,361,492.86 |
| EPIC/USDT:USDT | +41.84% | $2,818,006.50 |
| USELESS/USDT:USDT | +28.13% | $2,479,013.23 |
| LAB/USDT:USDT | +24.17% | $190,408,152.24 |
| MRVLSTOCK/USDT:USDT | +23.84% | $6,169,253.70 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SLX/USDT:USDT | below_1h_threshold | +4.05% | +4.18% |
| USELESS/USDT:USDT | below_1h_threshold | +3.58% | +3.71% |
| CLO/USDT:USDT | below_1h_threshold | +3.12% | +3.25% |
| CHIP/USDT:USDT | below_1h_threshold | +2.64% | +2.77% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.55% | +2.68% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
