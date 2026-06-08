# Decision Report

- generated_at: 2026-06-08T16:31:30.545822+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6084**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6084, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.53% | **-1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | -0.26% | **-0.09%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.53% | **+1.53%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.80% | **+1.35%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.17% | **+0.98%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1501件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T16:31:27.405787+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=63815.1
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.1 >= 65=1, 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PIPPIN/USDT:USDT | +20.98% | $19,908,872.65 |
| BLESS/USDT:USDT | +6.24% | $10,154,094.57 |
| ARKM/USDT:USDT | +4.05% | $1,022,090.33 |
| WLD/USDT:USDT | +3.81% | $93,609,445.99 |
| FHE/USDT:USDT | +3.40% | $1,403,973.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARKM/USDT:USDT | below_1h_threshold | +4.06% | +3.95% |
| WLD/USDT:USDT | below_1h_threshold | +3.71% | +3.61% |
| FHE/USDT:USDT | below_1h_threshold | +3.36% | +3.25% |
| H/USDT:USDT | below_1h_threshold | +3.25% | +3.14% |
| CHZ/USDT:USDT | below_1h_threshold | +3.21% | +3.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
