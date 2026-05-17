# Decision Report

- generated_at: 2026-05-17T10:28:49.259978+00:00
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

- 更新: 2026-05-17T10:28:47.100464+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=78508.0
- Funnel: target 760 → liquid 117 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +38.68% | $6,657,466.56 |
| CGPT/USDT:USDT | +26.71% | $2,246,510.11 |
| ASTEROID/USDT:USDT | +16.75% | $4,300,707.52 |
| AIA/USDT:USDT | +16.10% | $12,498,676.35 |
| VVV/USDT:USDT | +9.21% | $5,975,781.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CGPT/USDT:USDT | below_relative_strength | +5.06% | +4.69% |
| FF/USDT:USDT | below_1h_threshold | +2.32% | +1.94% |
| H/USDT:USDT | below_1h_threshold | +1.38% | +1.00% |
| NMR/USDT:USDT | below_1h_threshold | +1.15% | +0.78% |
| RUNE/USDT:USDT | below_1h_threshold | +1.07% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
