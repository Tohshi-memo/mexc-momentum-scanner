# Decision Report

- generated_at: 2026-05-09T18:57:39.400295+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3911**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3911, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.31% | **+0.09%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.78% | **+1.51%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.94% | **+1.26%** |
| MARKET_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_BB3S_LONG | 9/10 | 90.0% | +1.06% | **+0.95%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.33% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.27** / 初期 $100.00 (+8.27%)
- 確定: 195件 (Win 48 / Loss 65 / Flat 82) / skip 277件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +3.61%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `LIMIT_7PCT_LONG` EXPIRED account -0.13% 残高後 $108.27

## 4. Latest Market Context

- 更新: 2026-05-09T18:57:36.220379+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.10% price=80848.8
- Funnel: target 769 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RAVE/USDT:USDT | +17.98% | $23,414,837.01 |
| INX/USDT:USDT | +9.33% | $4,310,574.29 |
| JASMY/USDT:USDT | +8.50% | $6,039,958.39 |
| SATO/USDT:USDT | +8.44% | $4,839,983.90 |
| BIO/USDT:USDT | +7.74% | $1,188,034.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +4.35% | +4.25% |
| NIL/USDT:USDT | below_1h_threshold | +2.68% | +2.58% |
| BRETT/USDT:USDT | below_1h_threshold | +2.62% | +2.52% |
| JASMY/USDT:USDT | below_1h_threshold | +2.61% | +2.52% |
| DOGS/USDT:USDT | below_1h_threshold | +2.54% | +2.44% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
