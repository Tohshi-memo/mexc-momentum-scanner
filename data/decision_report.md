# Decision Report

- generated_at: 2026-05-31T22:15:00.928304+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5231**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5231, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.20% | **+0.77%** |
| LIMIT_5PCT | 13/20 | 65.0% | +0.89% | **+0.58%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |
| LIMIT_BB3S | 10/17 | 58.8% | +0.19% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +4.02% | **+2.21%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.95% | **+1.92%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.02% | **+1.72%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.20% | **+1.60%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.36% | **+1.51%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$135.49** / 初期 $100.00 (+35.49%)
- 確定: 866件 (Win 203 / Loss 256 / Flat 407) / skip 926件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $135.49

## 4. Latest Market Context

- 更新: 2026-05-31T22:14:57.983398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=73873.0
- Funnel: target 773 → liquid 129 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 89.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +75.19% | $14,483,238.33 |
| STG/USDT:USDT | +45.71% | $18,704,920.00 |
| HOME/USDT:USDT | +16.01% | $2,991,161.61 |
| ZORA/USDT:USDT | +13.85% | $1,549,914.77 |
| BIANRENSHENG/USDT:USDT | +11.85% | $3,121,372.08 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +1.36% | +1.34% |
| LIT/USDT:USDT | below_1h_threshold | +1.28% | +1.26% |
| LDO/USDT:USDT | below_1h_threshold | +1.20% | +1.18% |
| NEX/USDT:USDT | below_1h_threshold | +1.11% | +1.09% |
| RAVE/USDT:USDT | below_1h_threshold | +1.10% | +1.09% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
