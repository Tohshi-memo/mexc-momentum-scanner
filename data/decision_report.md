# Decision Report

- generated_at: 2026-05-11T18:43:21.781254+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4060**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4060, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.47%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.47% | **-0.47%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.24% | **+0.20%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.17% | **+1.00%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.77% | **+0.83%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.94% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 33件 (TP 8 / SL 22 / EXP 3)
- 最新: SIREN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.86** / 初期 $100.00 (+7.86%)
- 確定: 218件 (Win 54 / Loss 76 / Flat 88) / skip 403件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +4.09%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: B/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $107.86

## 4. Latest Market Context

- 更新: 2026-05-11T18:43:13.385898+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=81915.1
- Funnel: target 758 → liquid 194 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +13.85% | $1,647,495.65 |
| SKYAI/USDT:USDT | +12.15% | $29,924,685.71 |
| B/USDT:USDT | +11.58% | $30,762,965.92 |
| ASTEROID/USDT:USDT | +11.23% | $2,636,764.38 |
| PENGUIN/USDT:USDT | +10.47% | $2,215,176.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GIGA/USDT:USDT | below_relative_strength | +5.00% | +4.98% |
| BASED/USDT:USDT | below_1h_threshold | +4.59% | +4.56% |
| XNY/USDT:USDT | below_1h_threshold | +4.36% | +4.33% |
| USELESS/USDT:USDT | below_1h_threshold | +3.78% | +3.76% |
| B/USDT:USDT | below_1h_threshold | +3.53% | +3.51% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
