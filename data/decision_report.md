# Decision Report

- generated_at: 2026-06-11T07:27:01.707152+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6324**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6324, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.96% | **-1.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -2.31% | **-0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| MARKET_LONG | 20/20 | 100.0% | +1.80% | **+1.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.54% | **+1.78%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.34% | **+1.29%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +1.58% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1271件 (Win 319 / Loss 401 / Flat 551) / skip 1614件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T07:26:56.061434+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=62708.6
- Funnel: target 783 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +98.07% | $66,315,338.50 |
| AIO/USDT:USDT | +62.12% | $5,325,755.10 |
| BEAT/USDT:USDT | +54.42% | $211,845,644.84 |
| COLLECT/USDT:USDT | +40.16% | $1,539,064.14 |
| H/USDT:USDT | +38.87% | $11,642,210.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GALA/USDT:USDT | below_1h_threshold | +4.87% | +4.91% |
| BEAT/USDT:USDT | below_1h_threshold | +4.33% | +4.37% |
| WLD/USDT:USDT | below_1h_threshold | +2.80% | +2.84% |
| FIGHT/USDT:USDT | below_1h_threshold | +2.42% | +2.46% |
| XMR/USDT:USDT | below_1h_threshold | +1.66% | +1.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
