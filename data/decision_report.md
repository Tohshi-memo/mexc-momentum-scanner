# Decision Report

- generated_at: 2026-06-16T23:00:13.224501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6888**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6888, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.73%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.73% | **-0.73%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.37% | **+0.55%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.96% | **+0.24%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.15% | **+0.12%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_ATR | 13/20 | 65.0% | -0.39% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.91% | **+1.34%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.20% | **+0.96%** |
| MARKET_LONG | 20/20 | 100.0% | +0.89% | **+0.89%** |
| ASK_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.81% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$186.36** / 初期 $100.00 (+86.36%)
- 確定: 1761件 (Win 466 / Loss 553 / Flat 742) / skip 1688件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $186.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.75** / 初期 $100.00 (-2.25%)
- 確定: 162件 (Win 30 / Loss 31 / Flat 101) / skip 137件
- 成長率目線: 平均log -0.000141 / 幾何平均 -0.014% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0365 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $97.75

## 5. Latest Market Context

- 更新: 2026-06-16T23:00:08.633293+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=65747.8
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +20.62% | $2,524,036.95 |
| H/USDT:USDT | +18.74% | $56,560,909.98 |
| VELVET/USDT:USDT | +16.90% | $30,756,425.98 |
| UAI/USDT:USDT | +13.17% | $1,903,818.28 |
| ESPORTS/USDT:USDT | +12.39% | $2,191,300.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +3.26% | +3.25% |
| UAI/USDT:USDT | below_1h_threshold | +2.98% | +2.97% |
| TIA/USDT:USDT | below_1h_threshold | +2.58% | +2.57% |
| COAI/USDT:USDT | below_1h_threshold | +1.85% | +1.85% |
| BR/USDT:USDT | below_1h_threshold | +1.70% | +1.69% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
