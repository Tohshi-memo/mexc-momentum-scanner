# Decision Report

- generated_at: 2026-09-08T18:21:19.645891+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14017**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=14017, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.00% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.08% | **+0.05%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.30% | **-0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.15% | **+0.81%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +0.00% | **+0.00%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.19** / 初期 $100.00 (+912.19%)
- 確定: 5281件 (Win 1587 / Loss 1707 / Flat 1987) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,012.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.50** / 初期 $100.00 (+90.50%)
- 確定: 2620件 (Win 725 / Loss 622 / Flat 1273) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0156 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DOT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.12** / 初期 $100.00 (+20.12%)
- 確定: 2600件 (Win 762 / Loss 986 / Flat 852) / pending 6件 / skip 2884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000163 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $120.12

## 6. Latest Market Context

- 更新: 2026-09-08T18:21:09.734441+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.33% price=78729.0
- Funnel: target 1070 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +9.27% | $2,129,957.55 |
| DOGS/USDT:USDT | +8.36% | $1,310,048.16 |
| RAY/USDT:USDT | +5.35% | $2,246,394.37 |
| UAI/USDT:USDT | +3.65% | $13,503,411.15 |
| MARSCOIN/USDT:USDT | +3.60% | $2,771,836.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XAN/USDT:USDT | below_1h_threshold | +3.54% | +3.21% |
| RAY/USDT:USDT | below_1h_threshold | +3.53% | +3.19% |
| XPL/USDT:USDT | below_1h_threshold | +2.50% | +2.16% |
| LIT/USDT:USDT | below_1h_threshold | +1.68% | +1.34% |
| STRK/USDT:USDT | below_1h_threshold | +1.54% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
