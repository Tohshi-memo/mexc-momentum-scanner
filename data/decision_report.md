# Decision Report

- generated_at: 2026-07-06T13:32:07.182309+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8390**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8390, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 7/14 | 50.0% | +2.50% | **+1.25%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.16% | **+0.54%** |
| LIMIT_9PCT | 4/20 | 20.0% | +2.44% | **+0.49%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +2.44% | **+0.37%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +3.27% | **+0.82%** |
| ASK_LONG | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.04% | **+0.57%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.92% | **+0.55%** |
| MARKET_LONG | 20/20 | 100.0% | +0.43% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$101.57** / 初期 $100.00 (+1.57%)
- 確定トレード: 67件 (TP 23 / SL 43 / EXP 1)
- 最新: EPIC/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.57
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$317.13** / 初期 $100.00 (+217.13%)
- 確定: 2623件 (Win 832 / Loss 887 / Flat 904) / skip 2328件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_8PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VANRY/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $317.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.48** / 初期 $100.00 (+5.48%)
- 確定: 639件 (Win 152 / Loss 158 / Flat 329) / skip 1162件
- 成長率目線: 平均log +0.000084 / 幾何平均 +0.008% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASED/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account -0.26% 残高後 $105.48

## 5. Latest Market Context

- 更新: 2026-07-06T13:31:59.694370+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=61514.4
- Funnel: target 841 → liquid 167 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VANRY/USDT:USDT | +67.65% | $10,269,574.80 |
| YFI/USDT:USDT | +17.16% | $3,700,809.41 |
| TRIA/USDT:USDT | +16.50% | $2,186,241.95 |
| DEXE/USDT:USDT | +13.74% | $1,904,274.99 |
| TLM/USDT:USDT | +13.44% | $46,036,944.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANSEM/USDT:USDT | below_1h_threshold | +4.09% | +4.45% |
| TLM/USDT:USDT | below_1h_threshold | +3.09% | +3.45% |
| AALSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +2.78% |
| MONAD/USDT:USDT | below_1h_threshold | +1.80% | +2.15% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +1.77% | +2.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
