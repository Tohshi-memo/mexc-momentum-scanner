# Decision Report

- generated_at: 2026-05-07T00:52:51.840014+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3514**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3514, expectancy=-0.15%
- 直近20件 MARKET基準: n=20, expectancy=-0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.44% | **-0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.11% | **+0.39%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.09% | **+0.05%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.54% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.12% | **+1.41%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.55% | **+1.32%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| ASK_LONG | 20/20 | 100.0% | +0.68% | **+0.68%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.89% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$101.34** / 初期 $100.00 (+1.34%)
- 確定トレード: 19件 (TP 6 / SL 11 / EXP 2)
- 最新: TAG/USDT:USDT TP_HIT PnL +8.00% 残高後 $101.34
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$97.52** / 初期 $100.00 (-2.48%)
- 確定: 11件 (Win 0 / Loss 5 / Flat 6) / skip 64件
- 成長率目線: 平均log -0.002278 / 幾何平均 -0.228% per trade / maxDD +2.48%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $97.52

## 4. Latest Market Context

- 更新: 2026-05-07T00:52:46.036006+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.46% price=81015.3
- Funnel: target 766 → liquid 192 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOGS/USDT:USDT | +19.57% | $5,184,387.24 |
| ZEREBRO/USDT:USDT | +19.31% | $1,846,591.73 |
| PLAY/USDT:USDT | +19.10% | $19,060,909.16 |
| PENGUIN/USDT:USDT | +14.17% | $1,011,402.26 |
| LAB/USDT:USDT | +13.88% | $254,822,444.01 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VVV/USDT:USDT | below_1h_threshold | +4.02% | +4.48% |
| FHE/USDT:USDT | below_1h_threshold | +3.70% | +4.16% |
| B/USDT:USDT | below_1h_threshold | +2.70% | +3.16% |
| LYN/USDT:USDT | below_1h_threshold | +1.29% | +1.75% |
| ENSO/USDT:USDT | below_1h_threshold | +1.08% | +1.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
