# Decision Report

- generated_at: 2026-06-02T22:44:46.826016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5497**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5497, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.88%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.88% | **-0.88%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.96% | **+0.59%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.67% | **+0.47%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +2.41% | **+0.24%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.06% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +2.12% | **+1.51%** |
| MARKET_LONG | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.43% | **+1.14%** |
| ASK_LONG | 20/20 | 100.0% | +1.13% | **+1.13%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.39** / 初期 $100.00 (+30.39%)
- 確定: 976件 (Win 229 / Loss 300 / Flat 447) / skip 1082件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PIEVERSE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $130.39

## 4. Latest Market Context

- 更新: 2026-06-02T22:44:43.808244+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.88% price=66936.6
- Funnel: target 769 → liquid 154 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +33.54% | $12,880,808.20 |
| US/USDT:USDT | +27.59% | $6,998,778.34 |
| BBSTOCK/USDT:USDT | +15.80% | $1,728,127.58 |
| MRVLSTOCK/USDT:USDT | +14.36% | $14,929,484.54 |
| LIT/USDT:USDT | +13.85% | $6,566,490.53 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +4.37% | +5.26% |
| CLO/USDT:USDT | below_1h_threshold | +1.94% | +2.82% |
| AVGOSTOCK/USDT:USDT | below_1h_threshold | +1.84% | +2.73% |
| W/USDT:USDT | below_1h_threshold | +1.04% | +1.92% |
| GUN/USDT:USDT | below_1h_threshold | +0.29% | +1.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
